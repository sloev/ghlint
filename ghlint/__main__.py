try:
    from . import config
except (ValueError, ImportError):
    import config
try:
    from . import lint
except (ValueError, ImportError):
    import lint


def main():
    settings = config.settings()
    lint.run(settings)

if __name__ == "__main__":
    main()
