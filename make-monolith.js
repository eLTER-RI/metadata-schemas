const { default: $RefParser } = await import("@apidevtools/json-schema-ref-parser");
const fs = await import("fs")


// dereference these files by inlining referenced content (subschemas)
// omit file extension .json:
const files_main = [
    "eLTERMetadataSchemaDatasets",
    "eLTERMetadataSchemaExternalDatasets"
]

// dereference main files, stringify json result, save as "..._monolith.json":
await Promise.all(
    files_main.map(async (stub_filename) => {
        let outfile_name = `${stub_filename}_monolith_test.json`        
        let o_json = await $RefParser.dereference(`${stub_filename}.json`)
        fs.writeFile(outfile_name,
            JSON.stringify(o_json, null, 2),
            (error) => {if(error){console.error(error)}}
        )        
    })
);



