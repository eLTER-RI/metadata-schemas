library(jsonvalidate)
library(jsonlite)
library(listviewer) ## explore a list (such as a json) in the browser

## utilities to 
## - resolve subschema references into one monolithic main schema,
## - test instances against a given schema
## - explore a schema in the browser

## run in folder containing the main schemas
## (e. g. './eLTERMetadataSchemaDatasets.json')


## recursively include subschemas to obtain a monolithic big schema:
resolve_refs <- function(schema, base_path = '.') {
  if (is.list(schema)) {
    for (key in names(schema)) {
      if (key == "$ref") {
        ref_path <- schema[[key]]
        
        # Handle absolute & relative paths
        if (startsWith(ref_path, "http")) {
          ref_schema <- fromJSON(content(GET(ref_path), "text", encoding = "UTF-8"))
        } else {
          ref_schema <- fromJSON(file.path(base_path, ref_path))
        }
        
        # Recursively resolve the referenced schema
        schema <- resolve_refs(ref_schema, base_path)
      } else {
        # Recursively resolve other properties
        schema[[key]] <- resolve_refs(schema[[key]], base_path)
      }
    }
  }
  schema
}


## set up a validator to check instances (e. g. observations) against a schema:
validate_instance <- 
  json_validator(readLines('./eLTERMetadataSchemaExternalDatasets.json'),
                 engine = 'ajv',
                 strict = FALSE
  )
## use: `validate_instance({"foo": 2, "bar": "zinch"})`

## pull all subschemas into main schema and save as monolithic schema:
make_monolith <- \(fn){
  frags <- strsplit(fn, '\\.') |> unlist()
  outfile_name <- sprintf("%s_monolith.%s",
                          paste(head(frags, -1), collapse = ''),
                          tail(frags, 1)
  )
                          
readLines(fn) |> 
    parse_json() |> 
    resolve_refs() |> 
    toJSON(pretty = TRUE) |> 
    write(file.path('.', outfile_name))
}


make_monolith('./eLTERMetadataSchemaDatasets.json')
make_monolith('./eLTERMetadataSchemaExternalDatasets.json')

## check JSON tree with {listviewer}:
jsonedit(the_monolith)


