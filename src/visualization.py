color = (
    "purple"
    if cov >= 90
    else "red"
    if cov >= 80
    else "orange"
    if cov >= 70
    else "yellow"
    if cov >= 50
    else "blue"
)
