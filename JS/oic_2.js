function getNomenclatura(pais) {
    const nomenclaturas = {
      Argentina: "ARG",
      Brasil: "BRA",
      Chile: "CHI",
      Colombia: "COL",
      Ecuador: "ECU",
      Paraguay: "PAR",
      Peru: "PER",
      Uruguay: "URU",
      Venezuela: "VEN"
    };
  
    return nomenclaturas[pais] || "N/A";
  }