import { StreamingAdapter } from '../adapter';

class UpliveAdapter implements StreamingAdapter {
  name = 'uplive';
  private connected = false;

  async initialize(config: Record<string, any>) {
    // TODO: add Uplive SDK/API initialization
    console.info('UpliveAdapter.initialize', config);
  }

  async start(streamKey?: string) {
    console.info('UpliveAdapter.start', streamKey);
    this.connected = true;
  }

  async stop() {
    console.info('UpliveAdapter.stop');
    this.connected = false;
  }

  isConnected() {
    return this.connected;
  }
}

export default UpliveAdapter;
