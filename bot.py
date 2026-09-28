import importlib
import pkgutil
import logging

from telegram.ext import Application

from config import BOT_TOKEN


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


def load_plugins(application):

    import plugins

    for _, module_name, _ in pkgutil.iter_modules(
        plugins.__path__
    ):

        if module_name.startswith("_"):
            continue

        module = importlib.import_module(
            f"plugins.{module_name}"
        )

        if hasattr(module, "register"):
            module.register(application)

            logging.info(
                "Loaded plugin: %s",
                module_name
            )


def main():

    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing."
        )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    load_plugins(application)

    logging.info("Bot started.")

    application.run_polling(
        allowed_updates=["message", "callback_query", "my_chat_member"]
    )


if __name__ == "__main__":
    main()
