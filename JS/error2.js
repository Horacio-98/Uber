function parseErrorDetails(errorString) {
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(errorString, "text/xml");
  const errorElement = xmlDoc.getElementsByTagName("ns0:errorDetails")[0];
  const instanceElement = errorElement.getElementsByTagName("ns0:instance")[0];
  const instanceJson = JSON.parse(instanceElement.textContent.trim());
  const errorJson = instanceJson.error;
  const code = errorJson.code;
  const message = errorJson.message.value;
  const lang = errorJson.message.lang;
  var mensaje = message; 
  return mensaje; 
    
}