function fechaAct(dateString) {
  const [date, time] = dateString.split(' ');
  const [month, day, year] = date.split('-');
  const [hour, minute, second] = time.split(':');

  // const isoDate = '${year}-${month}-${day}T${hour}:${minute}:${second}Z';
  const isoFecha = year+"-"+month+"-"+day+"T"+hour+":"+minute+":"+second+"Z";
  var fecha = isoFecha; 
  return fecha; 
}

