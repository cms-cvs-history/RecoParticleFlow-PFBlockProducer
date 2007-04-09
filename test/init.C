{

gSystem->Load("libFWCoreFWLite.so");
gSystem->Load("libRecoParticleFlowPFBlockProducer.so");
AutoLibraryLoader::enable();
gSystem->Load("libCintex.so");
ROOT::Cintex::Cintex::Enable();

}
