DISCIPLINES = ["biology", "bioinformatics"]

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
        "v5.5.0-39-g561ea6c/utils/datavzrd"
