function encontrarError(parametro) {
    // Buscar el objeto "error" dentro del parámetro
    const errorObj = JSON.parse(parametro).error;
  
    // Extraer los valores de las propiedades "code", "message", "lang" y "value"
    const code = errorObj.code;
    const message = errorObj.message.value;
    const lang = errorObj.message.lang;
    const value = errorObj.message.value;

    var mensaje = message; 
  
    // Retornar los valores en un objeto
    return mensaje; 
  }