DISCIPLINES = ["bioinformatics", "anthropology", "physics", "social-science"]

rule all:
    input:
        expand(
            "results/{discipline}",
            discipline=DISCIPLINES
        )

rule datavzrd:
    input:
        config="resources/{discipline}.datavzrd.yaml"
    params:
        extra=""
    output:
        report(
            directory("results/{discipline}"),
            htmlindex="index.html",
        )
    log:
        "logs/datavzrd_report/{discipline}.log"
    wrapper:
        "v5.7.0-1-gc4d0692/utils/datavzrd"
