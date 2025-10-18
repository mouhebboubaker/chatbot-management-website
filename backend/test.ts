import dotenv from "dotenv";
dotenv.config();
import { drizzle } from "drizzle-orm/node-postgres";

import { eq } from "drizzle-orm";
import { users } from "./src/db/schema";

import axios, { AxiosError } from "axios";
import { response } from "express";
import { error } from "console";

const db = drizzle(process.env.DATABASE_URL!);

async function main() {


 
  try {
    let response = await axios.post(
      "http://localhost:3501/singUp",
      {
        nomPrenom: "test",
        email: "test",
        motDePasse: "test",
      },
      {}
    );
    console.log("response.data", response.data);
    console.log("response.headers", response.headers);
  } catch (error: unknown) {
    if (axios.isAxiosError(error) && error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log("error.response", error.response);
      console.log("error.response", error.response.data);
    } else if (axios.isAxiosError(error) && error.request) {
      // The request was made but no response was received
      // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
      // http.ClientRequest in node.js
    //   console.log("error.request", error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.log("Error", (error as {message:any }) .message);
    }

     
  }
}

main();
