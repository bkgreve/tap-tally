$(function () {
  let id = 0;
  $(".entry-selections").change(function () {
    const selection = $(this).val();
    $(".entry-selections").val(selection);
    id = selection;
  });

  $("#view-edit-entry").click(function () {
    window.location.href = "control-center/edit-entry/" + id;
  });
});
