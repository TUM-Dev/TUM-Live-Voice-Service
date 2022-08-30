from concurrent import futures
import grpc
import subtitles_pb2
import subtitles_pb2_grpc
from grpc_reflection.v1alpha import reflection
import logging
from config import Config
import os
import vosk


class SubtitleService(subtitles_pb2_grpc.SubtitlesServicer):
    def __init__(self, model_path: str):
        self.__generator = vosk.SubtitleGenerator(model_path)

    def Generate(self, request, context):
        self.__generator.generate(request.path)
        return subtitles_pb2.GenerateSubtitlesResponse(path=request.path)


def serve(cfg: Config, debug: bool = False):
    logging.basicConfig(level=(logging.INFO, logging.DEBUG)[debug])

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service = SubtitleService(
        model_path=cfg['vosk']['model']
    )
    subtitles_pb2_grpc.add_SubtitlesServicer_to_server(service, server)

    if debug:
        logging.debug('starting server with reflection activated.')
        service_names = (
            subtitles_pb2.DESCRIPTOR.services_by_name['Subtitles'].full_name,
            reflection.SERVICE_NAME,
        )
        reflection.enable_server_reflection(service_names, server)

    port = cfg['api']['port']
    logging.info(f'server listening at :{port}')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve(
        cfg=Config(os.environ["CONFIG_FILE"]),
        debug=os.environ["DEBUG"] != ""
    )
