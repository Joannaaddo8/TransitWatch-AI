# TransitWatch AI — Data Sources Statement

## Dataset Used
This prototype currently uses a synthetic transit operations dataset located at:

`backend/app/data/synthetic/transit_trips.csv`

## Dataset Type
Synthetic data.

## Purpose
The dataset simulates scheduled transit trips, actual delay values, service hours, and route-level performance patterns. It is used to demonstrate the TransitWatch AI data pipeline, including delay detection, KPI generation, route comparison, trend analysis, AI insights, and dashboard visualization.

## Fields
- route
- hour
- scheduled_time
- actual_delay

## Privacy Confirmation
This dataset contains no personally identifiable information (PII). It does not include passenger names, addresses, phone numbers, payment information, device identifiers, travel histories linked to individuals, or facial recognition data.

## Competition Compliance
The Transit Data Challenge permits synthetic data and open/public data sources. This prototype uses synthetic data for privacy-safe development and demonstration.