$(function () {
  const brewedOn = $("#brewed_on");
  const keggedOn = $("#kegged_on");
  const container =
    $(".bootstrap-iso form").length > 0 ? $(".bootstrap-iso form").parent() : "body";
  const options = {
    format: "mm/dd/yyyy",
    container: container,
    todayHighlight: true,
    autoclose: true,
  };
  brewedOn.datepicker(options);
  keggedOn.datepicker(options);
});
