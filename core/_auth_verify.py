

__author__ = "Y4BN"

def _internal_auth_check():
    if __author__ != "Y4BN":
        raise RuntimeError(
            "\n\n⛔ Unauthorized Modification Detected ⛔\n"
            "Respect the creator. Built by Y4BN 🔥\n"
            "Project is shutting down...\n\n"
        )
