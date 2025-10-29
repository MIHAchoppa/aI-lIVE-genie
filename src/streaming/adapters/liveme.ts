import { StreamingAdapter } from '../adapter';

class LiveMeAdapter implements StreamingAdapter {
  name = 'liveme';
  private connected = false;

  async initialize(config: Record<string, any>) {
    // TODO: add LiveMe API/SDK initialization
    console.info('LiveMeAdapter.initialize', config);
  }

  async start(streamKey?: string) {
    console.info('LiveMeAdapter.start', streamKey);
    this.connected = true;
  }

  async stop() {
    console.info('LiveMeAdapter.stop');
    this.connected = false;
  }

  isConnected() {
    return this.connected;
  }
}

export default LiveMeAdapter;
