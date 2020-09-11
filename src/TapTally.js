import { useEffect, useState } from "react";
import React from "react";
import "./App.css";
import TapEntry from "./components/TapEntry";
import Header from "./components/Header";

function TapTally() {
  const [tapEntries, setTapEntries] = useState([]);
  const [headerInfo, setHeaderInfo] = useState({});

  useEffect(() => {
    fetch("/api/entries")
      .then((res) => res.json())
      .then((data) => {
        setTapEntries(data.entries);
      });
    fetch("/api/header-info")
      .then((res) => res.json())
      .then((data) => {
        setHeaderInfo(data.headerInfo);
      });
  }, []);

  return (
    <>
      <div className="App">
        <div className="App-body">
          <Header data={headerInfo} />
          {tapEntries.map((entry, i) => (
            <TapEntry key={i} data={entry} />
          ))}
        </div>
      </div>
    </>
  );
}

export default TapTally;
