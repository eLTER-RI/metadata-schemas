import React from "react";

import { ContribBucketAggregationValuesElement } from "@lter_search";

const BucketAggregationValuesElement = ({ bucket, ...rest }) => {
  return (
    <ContribBucketAggregationValuesElement
      bucket={{ ...bucket, key: bucket.key.toString() }}
      {...rest}
    />
  );
};

export default BucketAggregationValuesElement;
