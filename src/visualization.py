def get_coverage_color(cov):

    if cov >= 90:
        return "purple"
    elif cov >= 80:
        return "red"
    elif cov >= 70:
        return "orange"
    elif cov >= 50:
        return "yellow"
    else:
        return "blue"
