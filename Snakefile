DISCIPLINES = ["biology", "bioinformatics", "anthropology"]

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
        "v5.5.2-17-g33d5b76/utils/datavzrd"
