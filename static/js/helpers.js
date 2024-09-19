function confirmSave() {
  return confirm('Are you sure you want to update this information?');
}

function openEditModal(affiliationId, doctorName, officeAddress, workingHours) {
  document.getElementById('affiliation_id').value = affiliationId;
  document.getElementById('doctor').value = doctorName;
  document.getElementById('office_address').value = officeAddress;
  document.getElementById('working_hours').value = workingHours;
}
