def verify(result,criteria):
    failed=[c for c,v in criteria.items() if not result.get(c)==v]
    return {"passed":len(failed)==0,"failed_checks":failed}
