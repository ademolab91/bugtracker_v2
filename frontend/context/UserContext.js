"use client";

import React, { createContext, useEffect, useState } from "react";
import ReactDOM from "react-dom";
import axios from "axios";

export const UserContext = createContext();
export const UserProvider = (props) => {
  const [token, setToken] = useState(
    typeof localStorage !== "undefined"
      ? localStorage.getItem("bugTrackerToken")
      : null
  );

  useEffect(() => {
    const fetchUser = async () => {
      const headers = {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      };
      const response = await axios.get("http://localhost:8000/users/me", {
        headers,
      });
      if (response.status !== 200) setToken(null);
      if (typeof localStorage !== "undefined")
        localStorage.setItem("bugTrackerToken", token);
    };
    fetchUser();
  }, [token]);

  return (
    <UserContext.Provider value={[token, setToken]}>
      {props.children}
    </UserContext.Provider>
  );
};
