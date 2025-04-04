[Back to model](_base.md)

# Actual eLTER Metadata model schema

```json
{
  "type": "object",
  "properties": {
    "$schema": {
      "type": "string"
    },
    "created": {
      "type": "string",
      "format": "date-time"
    },
    "deletion_status": {
      "type": "string"
    },
    "externalWorkflow": {
      "type": "object",
      "properties": {
        "defaultWorkflowTemplateId": {
          "type": "string"
        },
        "history": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "date": {
                "type": "string",
                "format": "date-time"
              },
              "status": {
                "type": "string"
              },
              "workflowHandle": {
                "type": "string"
              },
              "workflowTemplateId": {
                "type": "string"
              }
            }
          }
        }
      }
    },
    "id": {
      "type": "string"
    },
    "is_deleted": {
      "type": "boolean"
    },
    "is_published": {
      "type": "boolean"
    },
    "metadata": {
      "type": "object",
      "properties": {
        "additionalMetadata": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "value": {
                "type": "string"
              }
            }
          }
        },
        "alternateIdentifiers": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "alternateID": {
                "type": "string"
              },
              "alternateIDType": {
                "type": "string"
              }
            }
          }
        },
        "assetType": {
          "type": "object",
          "properties": {
            "assetTypeCode": {
              "type": "string"
            },
            "assetTypeURI": {
              "type": "string"
            }
          }
        },
        "contactPoints": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "contactEmail": {
                "type": "string"
              },
              "contactName": {
                "type": "string"
              }
            }
          }
        },
        "contributors": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "contributorAffiliation": {
                "type": "object",
                "properties": {
                  "entityID": {
                    "type": "object",
                    "properties": {
                      "entityID": {
                        "type": "string"
                      },
                      "entityIDSchema": {
                        "type": "string"
                      }
                    }
                  },
                  "entityName": {
                    "type": "string"
                  }
                }
              },
              "contributorEmail": {
                "type": "string"
              },
              "contributorFamilyName": {
                "type": "string"
              },
              "contributorGivenName": {
                "type": "string"
              },
              "contributorIDs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "entityID": {
                      "type": "string"
                    },
                    "entityIDSchema": {
                      "type": "string"
                    }
                  }
                }
              },
              "contributorType": {
                "type": "string"
              }
            }
          }
        },
        "creators": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "creatorAffiliation": {
                "type": "object",
                "properties": {
                  "entityID": {
                    "type": "object",
                    "properties": {
                      "entityID": {
                        "type": "string"
                      },
                      "entityIDSchema": {
                        "type": "string"
                      }
                    }
                  },
                  "entityName": {
                    "type": "string"
                  }
                }
              },
              "creatorEmail": {
                "type": "string"
              },
              "creatorFamilyName": {
                "type": "string"
              },
              "creatorGivenName": {
                "type": "string"
              },
              "creatorIDs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "entityID": {
                      "type": "string"
                    },
                    "entityIDSchema": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "dataLevel": {
          "type": "object",
          "properties": {
            "dataLevelCode": {
              "type": "string"
            },
            "dataLevelURI": {
              "type": "string"
            }
          }
        },
        "descriptions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "descriptionText": {
                "type": "string"
              },
              "descriptionType": {
                "type": "string"
              }
            }
          }
        },
        "geoLocations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "boundingBox": {
                "type": "object",
                "properties": {
                  "eastBoundLongitude": {
                    "type": "number"
                  },
                  "northBoundLatitude": {
                    "type": "number"
                  },
                  "southBoundLatitude": {
                    "type": "number"
                  },
                  "westBoundLongitude": {
                    "type": "number"
                  }
                }
              },
              "boundingPolygon": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "inPolygonPoint": {
                      "type": "object",
                      "properties": {
                        "latitude": {
                          "type": "number"
                        },
                        "longitude": {
                          "type": "number"
                        }
                      }
                    },
                    "points": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "latitude": {
                            "type": "number"
                          },
                          "longitude": {
                            "type": "number"
                          }
                        }
                      }
                    }
                  }
                }
              },
              "geographicDescription": {
                "type": "string"
              },
              "observationLocation": {
                "type": "object",
                "properties": {
                  "deimsLocationID": {
                    "type": "string"
                  },
                  "deimsLocationName": {
                    "type": "string"
                  }
                }
              },
              "point": {
                "type": "object",
                "properties": {
                  "latitude": {
                    "type": "number"
                  },
                  "longitude": {
                    "type": "number"
                  }
                }
              }
            }
          }
        },
        "habitatReferences": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "soHabitatCode": {
                "type": "string"
              },
              "soHabitatURI": {
                "type": "string"
              }
            }
          }
        },
        "keywords": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "keywordLabel": {
                "type": "string"
              },
              "keywordURI": {
                "type": "string"
              }
            }
          }
        },
        "language": {
          "type": "string"
        },
        "licenses": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "licenseCode": {
                "type": "string"
              },
              "licenseURI": {
                "type": "string"
              }
            }
          }
        },
        "methods": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "instrumentationDescription": {
                "type": "string"
              },
              "methodID": {
                "type": "string"
              },
              "qualityControlDescription": {
                "type": "string"
              },
              "sampling": {
                "type": "object",
                "properties": {
                  "samplingDescription": {
                    "type": "string"
                  },
                  "studyDescription": {
                    "type": "string"
                  }
                }
              },
              "steps": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "stepDescription": {
                      "type": "string"
                    },
                    "stepTitle": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "projects": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "projectID": {
                "type": "string"
              },
              "projectName": {
                "type": "string"
              }
            }
          }
        },
        "publicationDate": {
          "type": "string",
          "format": "date"
        },
        "relatedIdentifiers": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "relatedID": {
                "type": "string"
              },
              "relatedIDType": {
                "type": "string"
              },
              "relatedResourceType": {
                "type": "string"
              },
              "relationType": {
                "type": "string"
              }
            }
          }
        },
        "responsibleOrganizations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "organizationEmail": {
                "type": "string"
              },
              "organizationIDs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "entityID": {
                      "type": "string"
                    },
                    "entityIDSchema": {
                      "type": "string"
                    }
                  }
                }
              },
              "organizationName": {
                "type": "string"
              }
            }
          }
        },
        "siteReferences": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "siteID": {
                "type": "string"
              },
              "siteName": {
                "type": "string"
              }
            }
          }
        },
        "taxonomicCoverages": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "taxonomicClassification": {
                "type": "object",
                "properties": {
                  "taxonomicClassificationID": {
                    "type": "string"
                  },
                  "taxonomicCommonName": {
                    "type": "string"
                  },
                  "taxonomicRankName": {
                    "type": "string"
                  },
                  "taxonomicRankValue": {
                    "type": "string"
                  }
                }
              },
              "taxonomicDescription": {
                "type": "string"
              }
            }
          }
        },
        "temporalCoverages": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "endDate": {
                "type": "string",
                "format": "date"
              },
              "startDate": {
                "type": "string",
                "format": "date"
              }
            }
          }
        },
        "temporalResolution": {
          "type": "object",
          "properties": {
            "temporalResolutionUnit": {
              "type": "string"
            },
            "temporalResolutionValue": {
              "type": "integer"
            }
          }
        },
        "titles": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "titleLanguage": {
                "type": "string"
              },
              "titleText": {
                "type": "string"
              }
            }
          }
        },
        "version": {
          "type": "string"
        }
      }
    },
    "pid": {
      "type": "object",
      "properties": {
        "obj_type": {
          "type": "string"
        },
        "pid_type": {
          "type": "string"
        },
        "pk": {
          "type": "integer"
        },
        "status": {
          "type": "string"
        }
      }
    },
    "state": {
      "type": "string"
    },
    "state_timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "substring_search_field": {
      "type": "string"
    },
    "updated": {
      "type": "string",
      "format": "date-time"
    },
    "version_id": {
      "type": "integer"
    },
    "versions": {
      "type": "object",
      "properties": {
        "index": {
          "type": "integer"
        },
        "is_latest": {
          "type": "boolean"
        },
        "is_latest_draft": {
          "type": "boolean"
        },
        "latest_id": {
          "type": "string"
        },
        "latest_index": {
          "type": "integer"
        },
        "next_draft_id": {
          "type": "string"
        }
      }
    }
  }
}
```

[Back to model](_base.md)