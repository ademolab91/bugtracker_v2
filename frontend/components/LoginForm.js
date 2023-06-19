import React, { useState, useContext } from "react";
import ReactDOM from "react-dom";
import { useRouter } from "next/router";
import * as Yup from "yup";
import { Formik, Form } from "formik";
import { UserContext } from "@/context/UserContext";
import { MyTextInput } from "./SignUpForm";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [, setToken] = useContext(UserContext);
  const router = useRouter();

  return (
    <>
      <h1>Login</h1>
      <Formik
        initialValues={{
          email: "",
          password: "",
        }}
        validationSchema={Yup.object({
          email: Yup.string()
            .email("Invalid email address")
            .required("Required"),
          password: Yup.string().required("Required"),
        })}
        onSubmit={async (values, { setSubmitting }) => {
          setEmail(values.email);
          setPassword(values.password);
          setTimeout(() => {
            console.log(JSON.stringify(values, null, 2));
            setSubmitting(false);
          }, 400);
          const url = "http://127.0.0.1:8000/auth/login";
          const data = new URLSearchParams();
          data.append("grant_type", "");
          data.append("username", email);
          data.append("password", password);
          data.append("scope", "me items");
          data.append("client_id", "");
          data.append("client_secret", "");

          fetch(url, {
            method: "POST",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: data,
          })
            .then((response) => {
              if (response.ok) {
                return response.json();
              } else {
                throw new Error("Request failed with status:", response.status);
              }
            })
            .then((data) => {
              console.log("Response:", data);
              // Handle the response data
              setToken(data.access_token);
              router.push("/")
            })
            .catch((error) => {
              console.error("Error:", error);
              // Handle the error
            });
        }}
      >
        <Form>
          <MyTextInput
            label="Email Address"
            name="email"
            type="email"
            placeholder="jane@formik.com"
          />

          <MyTextInput
            label="Password"
            name="password"
            type="password"
            placeholder="*******"
          />

          <button type="submit">Login</button>
        </Form>
      </Formik>
    </>
  );
};

export default LoginForm;
