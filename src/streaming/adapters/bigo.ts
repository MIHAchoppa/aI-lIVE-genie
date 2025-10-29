import { StreamingAdapter } from '../adapter';

class BIGOAdapter implements StreamingAdapter {
  name = 'bigo';
  private connected = false;

  async initialize(config: Record<string, any>) {
    // TODO: implement BIGO initialization (API/SDK)
    console.info('BIGOAdapter.initialize', config);
  }

  async start(streamKey?: string) {
    console.info('BIGOAdapter.start', streamKey);
    this.connected = true;
  }

  async stop() {
    console.info('BIGOAdapter.stop');
    this.connected = false;
  }

  isConnected() {
    return this.connected;
  }
}

export default BIGOAdapter;
