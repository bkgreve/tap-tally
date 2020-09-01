import React from "react";
import logo from "./logo.svg";
import "./App.css";
import TapEntry from "./components/TapEntry";

function TapTally() {
  return (
    <div className="App">
      <header className="App-header">
        Tap Tally: Digital Tap List and Keg Level Monitor
        <TapEntry />
        <TapEntry />
        <TapEntry />
        <TapEntry />
      </header>
    </div>
  );
}

export default TapTally;
