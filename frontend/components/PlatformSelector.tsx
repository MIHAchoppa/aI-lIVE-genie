import React from 'react';

type Platform = 'spotify' | 'tiktok' | 'bigo' | 'youtube' | 'uplive' | 'liveme';

interface Props {
  value?: Platform;
  onChange?: (platform: Platform, streamKey?: string) => void;
}

export const PlatformSelector: React.FC<Props> = ({ value = 'spotify', onChange }) => {
  const [platform, setPlatform] = React.useState<Platform>(value);
  const [streamKey, setStreamKey] = React.useState('');

  function submit() {
    onChange?.(platform, streamKey || undefined);
  }

  return (
    <div>
      <label>
        Platform
        <select value={platform} onChange={(e) => setPlatform(e.target.value as Platform)}>
          <option value="spotify">Spotify</option>
          <option value="tiktok">TikTok</option>
          <option value="bigo">BIGO</option>
          <option value="youtube">YouTube Live</option>
          <option value="uplive">Uplive</option>
          <option value="liveme">LiveMe</option>
        </select>
      </label>

      <label>
        Stream Key / Token
        <input value={streamKey} onChange={(e) => setStreamKey(e.target.value)} placeholder="stream key or token" />
      </label>

      <button onClick={submit}>Connect</button>
    </div>
  );
};

export default PlatformSelector;
