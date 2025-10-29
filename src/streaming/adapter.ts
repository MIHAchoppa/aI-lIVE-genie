export interface StreamingAdapter {
  name: string;
  initialize(config: Record<string, any>): Promise<void>;
  start(streamKey?: string): Promise<void>;
  stop(): Promise<void>;
  isConnected(): boolean;
}
export default StreamingAdapter;
