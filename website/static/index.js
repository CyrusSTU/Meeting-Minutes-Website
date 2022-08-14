function deleteMinute(event, id) {
  if (event) {
      event.preventDefault();
  }

  // Remove the minute from the table
  document.getElementById("minute-" + id).remove();
}