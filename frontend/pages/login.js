import LoginForm from "@/components/LoginForm";
import Link from "next/link";
import { useContext, useEffect } from "react";
import { useRouter } from "next/router";
import { UserContext } from "@/context/UserContext";

export default function LoginPage() {
  const [token] = useContext(UserContext);
  const router = useRouter();

  useEffect(() => {
    if (token) router.push("/");
  }, [token, router]);
  return (
    <div>
      <LoginForm />
      <p>
        Don't have an account? sign up <Link href="./signup">here</Link>
      </p>
    </div>
  );
}
