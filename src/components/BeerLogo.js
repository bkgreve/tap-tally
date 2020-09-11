import React from "react";

function BeerLogo(props) {
  const imageName = props.name;
  const imageLocation = window.location.hostname + "/" + imageName;
  return (
    <div className="col-md-2 my-auto">
      <img className="image-beer-logo" src={imageName} />
    </div>
  );
}

export default BeerLogo;
