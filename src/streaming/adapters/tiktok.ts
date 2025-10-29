import { StreamingAdapter } from '../adapter';

class TikTokAdapter implements StreamingAdapter {
  name = 'tiktok';
  private connected = false;

  async initialize(config: Record<string, any>) {
    // TODO: implement OAuth/SDK initialization for TikTok Live
    console.info('TikTokAdapter.initialize', config);
  }

  async start(streamKey?: string) {
    // TODO: implement logic to start streaming to TikTok using streamKey or SDK
    console.info('TikTokAdapter.start', streamKey);
    this.connected = true;
  }

  async stop() {
    console.info('TikTokAdapter.stop');
    this.connected = false;
  }

  isConnected() {
    return this.connected;
  }
}

export default TikTokAdapter;
