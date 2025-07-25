const fs = require('fs')

const infile_names = [
    'eLTERMetadataSchemaDatasets_monolith.json',
    'eLTERMetadataSchemaExternalDatasets_monolith.json'
]

// run for each monolith specified in infile_names:
Promise.all(
    infile_names.map(async (infile_name) => {
        // read infile and parse content as JSON object:
        const o = JSON.parse(fs.readFileSync(infile_name))
        // object nodes whose contents should be exported as dedicated subschemas:
        const nodes_subschema = o.properties.metadata.properties
        // write each node's content to a subschema file:
        Object.keys(nodes_subschema).map(k => {
            let content = nodes_subschema[k]
            let outfile_name = `subschemas/${k}.json`
            fs.writeFile(outfile_name,
                JSON.stringify(content, null, 2),
                (error) => {if(error){console.error(error)}}
            )
        })
    })
);