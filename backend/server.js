const express = require("express");
const cors = require("cors");
const scrapeRoutes = require("./routes/scrapeRoutes");
const app = express();

app.use(cors());
app.use(express.json());
app.use("/api", scrapeRoutes);

const PORT = 5000;
app.listen(PORT, () => console.log(`✅ Server running on port ${PORT}`));
