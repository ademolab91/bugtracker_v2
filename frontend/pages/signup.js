import SignUpForm from "@/components/SignUpForm";
import Link from "next/link";
import { useContext, useEffect } from "react";
import { useRouter } from "next/router";
import { UserContext } from "@/context/UserContext";

export default function SignUpPage() {
  const [token] = useContext(UserContext);
  const router = useRouter()

  useEffect(() => {
    if (token) router.push("/")
  }, [token])
  return (
    <div>
      <SignUpForm />
      <p>
        Already have an account? login <Link href="./login">here</Link>
      </p>
    </div>
  );
}
