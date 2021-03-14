from app.core.exceptions import CM

class ERR:
    ERROR_SAMPLE = CM(0, "Error Sample: %(msg)s")
    ERROR_SAMPLE2 = CM(0, "Error kaka")
    ERROR_API = CM(1000, "Error API: %(api)s")
    ERROR_DAO = CM(1001, "Error DAO: %(dao)s:%(api)s")