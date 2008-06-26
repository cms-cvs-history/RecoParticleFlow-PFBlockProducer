import FWCore.ParameterSet.Config as cms

particleFlowBlock = cms.EDProducer("PFBlockProducer",

    # resolution maps
    pf_resolution_map_HCAL_eta = cms.string('RecoParticleFlow/PFBlockProducer/data/resmap_HCAL_eta.dat'),
    pf_resolution_map_HCAL_phi = cms.string('RecoParticleFlow/PFBlockProducer/data/resmap_HCAL_phi.dat'),
    pf_resolution_map_ECAL_eta = cms.string('RecoParticleFlow/PFBlockProducer/data/resmap_ECAL_eta.dat'),
    pf_resolution_map_ECAL_phi = cms.string('RecoParticleFlow/PFBlockProducer/data/resmap_ECAL_phi.dat'),
                                   
    # max chi2 for element associations in PFBlocks
    pf_chi2_ECAL_Track = cms.double(100.0),
    pf_chi2_HCAL_Track = cms.double(100.0),
    pf_chi2_PS_Track = cms.double(100.0),
    pf_chi2_ECAL_HCAL = cms.double(10.0),
    pf_chi2_PSH_PSV = cms.double(5.0),
    pf_chi2_ECAL_PS = cms.double(100.0),

    pf_multilink = cms.bool(True),

    # verbosity 
    verbose = cms.untracked.bool(False),
                                   

    # input clusters
    PFClustersECAL = cms.InputTag("particleFlowClusterECAL"),
    PFClustersHCAL = cms.InputTag("particleFlowClusterHCAL"),
    PFClustersPS = cms.InputTag("particleFlowClusterPS"),

    # input tracks
    GsfRecTracks = cms.InputTag("pfTrackElec"),
    RecTracks = cms.InputTag("elecpreid"),

    # input nuclear interactions 
    PFNuclear = cms.InputTag("pfNuclear"),
    useNuclear = cms.bool(False),

    # input muons
    RecMuons = cms.InputTag("muons"),

    # input conversions
    PFConversions = cms.InputTag("pfConversions"),
    useConversions = cms.bool(False),

    # Track Quality Cut: Tracks are kept if DPt/Pt < Cut
    pf_DPtoverPt_Cut = cms.double(999.9),
                                   

    debug = cms.untracked.bool(False)
)


