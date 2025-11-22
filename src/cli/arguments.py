from argparse import ArgumentParser, Namespace
from dataclasses import dataclass

from cli.common import PROGRAM_NAME, PROGRAM_DESCRIPTION
from cli.utils import is_valid_windows_path


@dataclass
class Arguments:
    config_file_path: str
    debug: bool


class ArgumentParserManager:
    def __init__(self):
        self._argument_parser: ArgumentParser = ArgumentParserManager._build_argument_parser()
        self._namespace: Namespace | None = None
        self._arguments: Arguments | None = None

    @staticmethod
    def _build_argument_parser() -> ArgumentParser:
        argument_parser = ArgumentParser(
            prog=PROGRAM_NAME,
            description=PROGRAM_DESCRIPTION
        )
        argument_parser.add_argument(
            "config_file_path",
            default=".",
            type=str,
            help="Path to config file",
        )
        argument_parser.add_argument(
            "-d", "--debug",
            action="store_true",
            help="Enable debug mode",
        )
        return argument_parser

    def _validate_namespace(self, namespace: Namespace):
        if not is_valid_windows_path(namespace.config_file_path):
            self._argument_parser.error("Invalid config file path")

    def _build_namespace(self) -> Namespace:
        namespace = self._argument_parser.parse_args()
        self._validate_namespace(namespace)
        return namespace

    def _get_namespace(self) -> Namespace:
        if self._namespace is None:
            self._namespace = self._build_namespace()
        return self._namespace

    def _build_arguments(self) -> Arguments:
        namespace = self._get_namespace()
        return Arguments(
            config_file_path=namespace.config_file_path,
            debug=namespace.debug,
        )

    def _get_arguments(self) -> Arguments:
        if self._arguments is None:
            self._arguments = self._build_arguments()
        return self._arguments

    @property
    def arguments(self) -> Arguments:
        return self._get_arguments()
