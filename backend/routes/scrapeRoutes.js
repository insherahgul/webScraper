const express = require("express");
const fs = require("fs");
const path = require("path");
const router = express.Router();

router.post("/scrap", (req, res) => {
  const { url } = req.body;

  // JSON data to save
  const data = {
    url,
    message: "Website scrapped"
  };

  // Define file path
  const filePath = path.join(__dirname, "../scraped.json");

  // Write JSON file
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));

  // Send file to frontend for download
  res.download(filePath, "scraped.json", (err) => {
    if (err) {
      console.error(err);
      res.status(500).json({ message: "Error generating file" });
    }
  });
});

module.exports = router;
