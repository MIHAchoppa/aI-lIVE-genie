import { StreamingAdapter } from '../adapter';

class YouTubeAdapter implements StreamingAdapter {
  name = 'youtube';
  private connected = false;

  async initialize(config: Record<string, any>) {
    // TODO: integrate YouTube Live API (OAuth2) and prepare liveBroadcast/liveStream
    console.info('YouTubeAdapter.initialize', config);
  }

  async start(streamKey?: string) {
    console.info('YouTubeAdapter.start', streamKey);
    this.connected = true;
  }

  async stop() {
    console.info('YouTubeAdapter.stop');
    this.connected = false;
  }

  isConnected() {
    return this.connected;
  }
}

export default YouTubeAdapter;
