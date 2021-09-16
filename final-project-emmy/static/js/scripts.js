const saved = () => {
  alert(
    "Thank you for contacting us!\nWe will get back to you via your email address"
  );
};

const readMore = (btn, id, type) => {
  btn.innerHTML = "Read Less";
  $("#more" + type + id).removeClass("d-none");
  $("#less" + type + id).addClass("d-none");
  btn.setAttribute("onclick", "readLess(this,'" + id + "','" + type + "')");
};

const readLess = (btn, id, type) => {
  btn.innerHTML = "Read More";
  $("#more" + type + id).addClass("d-none");
  $("#less" + type + id).removeClass("d-none");
  btn.setAttribute("onclick", "readMore(this,'" + id + "','" + type + "')");
};

const handleScroll = (section) =>
  $("html, body").animate({ scrollTop: $("#" + section).offset().top }, 1000);
