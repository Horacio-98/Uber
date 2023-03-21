function parseString(inputString) {
    var splitArray = inputString.split('~~');
    var lastString = splitArray[splitArray.length - 1];
    var resultArray = lastString.split('-');
    return [resultArray[0], resultArray[1], resultArray[2], resultArray[3], resultArray[4]];
  }