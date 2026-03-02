# Registack v0.1.0 – Working Draft

⚠️ Status: WORKING DRAFT – v0.1

This repository contains the working draft specifications of:

- ACCF – Alignment & Constraint Control Framework
- MRP – Model Registration Protocol
- MAP – Model Audit Protocol
- MIP – Model Incident Protocol

Registack is designed as governance-layer infrastructure for AI systems.

All modifications occur via pull request governance.
All releases are cryptographically signed.


schemas/v0.1/
  mrp/
    mrp.registration.schema.json
    mrp.validation.schema.json
    mrp.revocation.schema.json
    mrp.insurance_attestation.schema.json
  accf/
    accf.constraints.schema.json
    accf.control_catalog.schema.json
    accf.enforcement_result.schema.json
  map/
    map.tool.schema.json
    map.policy.schema.json
    map.telemetry_event.schema.json
    map.audit_packet.schema.json   (your current map.v0.1 fits here)
  mip/
    mip.incident_report.schema.json
    mip.notification.schema.json
    mip.closure.schema.json
  common/
    common.identifiers.schema.json
    common.signatures.schema.json
    common.policy_ref.schema.json
    common.evidence_ref.schema.json
