import { UserContext } from "@/context/UserContext";
import { useContext } from "react";
import { useRouter } from "next/router";

const LogOut = () => {
  const [, setToken] = useContext(UserContext);
  const router = useRouter();
  const handleClick = () => {
    setToken(null);
    localStorage.removeItem("bugTrackerToken")
    router.push("./login");
  };
  return <button onClick={handleClick}>Logout</button>;
};

export default LogOut;
