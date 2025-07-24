const { default: $RefParser } = require("@apidevtools/json-schema-ref-parser");
const fs = require("fs")
const path = require("path");

// dereference these files by inlining referenced content (subschemas)
// omit file extension .json:
const files_main = [
    "eLTERMetadataSchemaDatasets",
    "eLTERMetadataSchemaExternalDatasets"
]


// dereference main files, stringify json result, save as "..._monolith.json":
Promise.all(
    files_main.map(async (stub_filename) => {
        let outfile_name = path.join(
            __dirname, `${stub_filename}_monolith.json`
        )        
        let o_json = await $RefParser.dereference(`${stub_filename}.json`)
        fs.writeFile(outfile_name,
            JSON.stringify(o_json, null, 2),
            (error) => {if(error){console.error(error)}}
        )        
    })
);
