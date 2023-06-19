import { useContext, useEffect } from "react";
import { UserContext } from "@/context/UserContext";
import { useRouter } from "next/router";
import Header from "@/components/Header";

export default function Home() {
  const [token] = useContext(UserContext);
  const router = useRouter();

  useEffect(() => {
    if (!token) router.push("./login");
  }, [token, router]);
  return (
    <div>
      <Header />
      <h1>Home Page</h1>
    </div>
  );
}
