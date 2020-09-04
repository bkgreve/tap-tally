import React from "react";
import logo from "./logo.svg";
import "./App.css";
import TapEntry from "./components/TapEntry";
import Header from "./Header";

function TapTally() {
  return (
    <div className="App">
      <div className="App-header">
        <Header />
        <TapEntry />
        <TapEntry />
        <TapEntry />
        <TapEntry />
      </div>
    </div>
  );
}

export default TapTally;
