import React from "react";
import ReactDOM from "react-dom";
import { useRouter } from "next/router";
import { Formik, Form, useField } from "formik";
import * as Yup from "yup";
import axios from "axios";

const MyTextInput = ({ label, ...props }) => {
  // useField() returns [formik.getFieldProps(), formik.getFieldMeta()]
  // which we can spread on <input>. We can use field meta to show an error
  // message if the field is invalid and it has been touched (i.e. visited)
  const [field, meta] = useField(props);
  return (
    <>
      <label htmlFor={props.id || props.name}>{label}</label>
      <input className="text-input" {...field} {...props} />
      {meta.touched && meta.error ? (
        <div className="error">{meta.error}</div>
      ) : null}
    </>
  );
};

const MyCheckbox = ({ children, ...props }) => {
  // React treats radios and checkbox inputs differently from other input types: select and textarea.
  // Formik does this too! When you specify `type` to useField(), it will
  // return the correct bag of props for you -- a `checked` prop will be included
  // in `field` alongside `name`, `value`, `onChange`, and `onBlur`
  const [field, meta] = useField({ ...props, type: "checkbox" });
  return (
    <div>
      <label className="checkbox-input">
        <input type="checkbox" {...field} {...props} />
        {children}
      </label>
      {meta.touched && meta.error ? (
        <div className="error">{meta.error}</div>
      ) : null}
    </div>
  );
};

const MySelect = ({ label, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div>
      <label htmlFor={props.id || props.name}>{label}</label>
      <select {...field} {...props} />
      {meta.touched && meta.error ? (
        <div className="error">{meta.error}</div>
      ) : null}
    </div>
  );
};

// And now we can use these
const SignupForm = () => {
  const router = useRouter()
  return (
    <>
      <h1>Sign Up!</h1>
      <Formik
        initialValues={{
          firstName: "",
          lastName: "",
          email: "",
          role: "",
          password: "",
          confirmPassword: "",
        }}
        validationSchema={Yup.object({
          firstName: Yup.string()
            .max(15, "Must be 15 characters or less")
            .required("Required"),
          lastName: Yup.string()
            .max(20, "Must be 20 characters or less")
            .required("Required"),
          email: Yup.string()
            .email("Invalid email address")
            .required("Required"),
          role: Yup.string()
            .oneOf(
              ["developer", "project_manager", "qa_tester", "other"],
              "Invalid Job Type"
            )
            .required("Required"),
          password: Yup.string().required("Required"),
          confirmPassword: Yup.string()
            .oneOf([Yup.ref("password")], "Password must match")
            .required("Required"),
        })}
        onSubmit={(values, { setSubmitting }) => {
          const data = {
            name: values["firstName"] + " " + values["lastName"],
            email: values["email"],
            password: values["password"],
            role: values["role"],
          };
          setTimeout(() => {
            console.log(data);
            setSubmitting(false);
          }, 400);
          const url = `http://localhost:8000/users/signup`;
          console.log(`URL: ${url}`);
          axios
            .post(url, data)
            .then((response) => {
              console.log(`Response: ${response}`);
              router.push("./login")
            })
            .catch((error) => {
              console.log("There was an error!", error.response);
              // alert("Email already exists");
            });
        }}
      >
        <Form>
          <MyTextInput
            label="First Name"
            name="firstName"
            type="text"
            placeholder="Ademola"
          />

          <MyTextInput
            label="Last Name"
            name="lastName"
            type="text"
            placeholder="Balogun"
          />

          <MyTextInput
            label="Email Address"
            name="email"
            type="email"
            placeholder="ademolabalogun91@gmail.com"
          />

          <MySelect label="Role" name="role">
            <option value="">Select a job type</option>
            <option value="developer">Developer</option>
            <option value="project_manager">Project Manager</option>
            <option value="qa_tester">QA Tester</option>
            <option value="other">Other</option>
          </MySelect>

          <MyTextInput
            label="Password"
            name="password"
            type="password"
            placeholder="********"
          />

          <MyTextInput
            label="Confirm Password"
            name="confirmPassword"
            type="password"
            placeholder="********"
          />

          <button type="submit">Submit</button>
        </Form>
      </Formik>
    </>
  );
};

export default SignupForm;
export { MyTextInput };
